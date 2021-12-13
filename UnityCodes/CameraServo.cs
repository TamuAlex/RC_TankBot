using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RabbitMQ.Client;
using System.Text;
using Valve.VR;
/***********************************************************
 *                                                         *
 *                         Authors:                        *
 *   Alejandro Ortega Martinez: alejandro.ormar@gmail.com  *
 *   Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es         *
 *                                                         *
 ***********************************************************/

/************************************************************
 *        Script for connecting the movement of the         *
 *        camera servos in the raspberry Pi robot           *
 *        with a unity projec tusing the AMQP protocol,     *
 *        the RabbitMQ library, and hosting the broker in   *
 *        cloudamp.com                                      *
 ************************************************************/


public class CameraServo : MonoBehaviour
{
    //Declaration for VR inputs

    public SteamVR_Action_Vector2 LeftJoystickAction;

    public SteamVR_Action_Vector2 RightJoystickAction;

    //Declaration of flags for only sending a message per movement, not one per frame, for not flooding the queue
    bool upFlag;
    bool downFlag;
    bool leftFlag;
    bool rightFlag;


    //Declaration of the different messages that we can send to the robot
    byte[] msgUpOn;
    byte[] msgUpOff;
    byte[] msgDwnOn;
    byte[] msgDwnOff;
    byte[] msgLftOn;
    byte[] msgLftOff;
    byte[] msgRgthOn;
    byte[] msgRghtOff;

    //Declaration of the RabbitMQ channel
    IModel ch;
    IBasicProperties properties;



    // Start is called before the first frame update
    void Start()
    {
        //Declaring the amqp server Address
        string serverAddress = "amqps://zvaqximc:I2_yD3JdVLcdqBIdH__EUToUUdEVSsWf@fish.rmq.cloudamqp.com/zvaqximc";


        //Initialize the flags according to the servos state at the start of the script (stopped)
        upFlag = false;
        downFlag = false;
        leftFlag = false;
        rightFlag = false;

        // Possible messages that can be sent to the queue
        msgUpOn = Encoding.UTF8.GetBytes("up");
        msgUpOff = Encoding.UTF8.GetBytes("sup");
        msgDwnOn = Encoding.UTF8.GetBytes("down");
        msgDwnOff = Encoding.UTF8.GetBytes("sdown");
        msgLftOn = Encoding.UTF8.GetBytes("left");
        msgLftOff = Encoding.UTF8.GetBytes("sleft");
        msgRgthOn = Encoding.UTF8.GetBytes("right");
        msgRghtOff = Encoding.UTF8.GetBytes("sright");

        //Establish the connection to the AMQP server
        ConnectionFactory cf = new ConnectionFactory();
        cf.Uri = serverAddress;
        IConnection conn = cf.CreateConnection();
        ch = conn.CreateModel();

    }

    // Update is called once per frame

    void Update()
    {
        //VR inputs

        Vector2 LeftJoystickValue = LeftJoystickAction.GetAxis(SteamVR_Input_Sources.Any);

        Vector2 RightJoyStickValue = RightJoystickAction.GetAxis(SteamVR_Input_Sources.Any);

        //Up movement, pressing the up arrow key
        //When the up arrow key is pressed
        if (RightJoyStickValue.y > 0.75)
        {
            //It cheks if it was not already pressed (this is used for not sending a message every frame, and flood the queue)
            if (!upFlag)
            {
                //It sends the message of lifting up the camera
                Debug.Log("Movemos Arriba");
                ch.BasicPublish("", "CameraServos", null, msgUpOn);
                upFlag = true;
            }
            //If the up arrow key is not pressed, we chek if the previous frame it was pressed
        }
        else if (upFlag)
        {
            //If so, a message telling the servo to stop is sended
            Debug.Log("Paramos arriba");
            ch.BasicPublish("", "CameraServos", null, msgUpOff);
            upFlag = false;

        }




        //Down movement, pressing the down key arrow
        if (RightJoyStickValue.y < -0.75)
        {
            if (!downFlag)
            {
                Debug.Log("Movemos abajo");
                ch.BasicPublish("", "CameraServos", null, msgDwnOn);
                downFlag = true;
            }
        }
        else if (downFlag)
        {
            Debug.Log("Paramos abajo");
            ch.BasicPublish("", "CameraServos", null, msgDwnOff);
            downFlag = false;
        }




        //Left movement, pressing the left key arrow
        if (RightJoyStickValue.x < -0.75)
        {
            if (!leftFlag)
            {
                Debug.Log("Movemos izquierda");
                ch.BasicPublish("", "CameraServos", null, msgLftOn);
                leftFlag = true;
            }
        }
        else if (leftFlag)
        {
            Debug.Log("Paramos izq");
            ch.BasicPublish("", "CameraServos", null, msgLftOff);
            leftFlag = false;
        }




        //Right movement, pressing the right key arrow
        if (RightJoyStickValue.x > 0.75)
        {
            if (!rightFlag)
            {
                Debug.Log("Movemos derecha");
                ch.BasicPublish("", "CameraServos", null, msgRgthOn);
                rightFlag = true;
            }
        }
        else if (rightFlag)
        {
            Debug.Log("Paramos dcha");
            ch.BasicPublish("", "CameraServos", null, msgRghtOff);
            rightFlag = false;
        }
    }

    private void OnApplicationQuit()
    {
        //When exiting the app, all movements are stopped
        ch.BasicPublish("", "CameraServos", null, msgUpOff);
        ch.BasicPublish("", "CameraServos", null, msgDwnOff);
        ch.BasicPublish("", "CameraServos", null, msgLftOff);
        ch.BasicPublish("", "CameraServos", null, msgRghtOff);

        //The queue is purged, in order to not let any unaknowledge message waiting for the next time the robot connects to it.
        ch.QueuePurge("CameraServos");
        ch.Close();

    }
}