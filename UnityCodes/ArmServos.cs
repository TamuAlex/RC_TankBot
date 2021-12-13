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
 *        claw servos in the raspberry Pi robot             *
 *        with a unity projec tusing the AMQP protocol,     *
 *        the RabbitMQ library, and hosting the broker in   *
 *        cloudamp.com                                      *
 ************************************************************/

public class ArmServos : MonoBehaviour
{
    //Declaration for VR inputs

    public SteamVR_Action_Vector2 LeftJoystickAction;

    public SteamVR_Action_Vector2 RightJoystickAction;

    public SteamVR_Action_Boolean grip1Left;

    public SteamVR_Action_Boolean grip1Right;

    public SteamVR_Action_Boolean grip2Left;

    public SteamVR_Action_Boolean grip2Right;

    public SteamVR_Action_Boolean yButton;
    public SteamVR_Action_Boolean bButton;

    public SteamVR_Action_Boolean xButton;
    public SteamVR_Action_Boolean aButton;




    //Declaration of flags for only sending a message per movement, not one per frame, for not flooding the queue
    bool elbowUpFlag;
    bool elbowDownFlag;
    bool wristUpFlag;
    bool wristDownFlag;
    bool turnLeftFlag;
    bool turnRightFlag;
    bool openClawFlag;
    bool closeClawFlag;


    //Declaration of the different messages that we can send to the robot
    byte[] msgElbowUp;
    byte[] msgElbowDown;
    byte[] msgElbowStop;

    byte[] msgWristUp;
    byte[] msgWristDown;
    byte[] msgWristStop;

    byte[] msgTurnRight;
    byte[] msgTurnLeft;
    byte[] msgTurnStop;

    byte[] msgOpenClaw;
    byte[] msgCloseClaw;
    byte[] msgIdleClaw;


    //Declaration of the RabbitMQ channel
    IModel ch;
    IBasicProperties properties;

    // Start is called before the first frame update
    void Start()
    {
        string serverAddress = "amqps://zvaqximc:I2_yD3JdVLcdqBIdH__EUToUUdEVSsWf@fish.rmq.cloudamqp.com/zvaqximc";


        //Initialize the flags according to the servos state at the start of the script (stopped)
        elbowUpFlag = false;
        elbowDownFlag = false;
        wristUpFlag = false;
        wristDownFlag = false;
        turnLeftFlag = false;
        turnRightFlag = false;
        openClawFlag = false;
        closeClawFlag = false;


        //The different messages that can be sent, encoded in a byte stream
        msgElbowUp = Encoding.UTF8.GetBytes("uS1");
        msgElbowDown = Encoding.UTF8.GetBytes("dS1");
        msgElbowStop = Encoding.UTF8.GetBytes("sS1");

        msgWristUp = Encoding.UTF8.GetBytes("uS2");
        msgWristDown = Encoding.UTF8.GetBytes("dS2");
        msgWristStop = Encoding.UTF8.GetBytes("sS2");

        msgTurnRight = Encoding.UTF8.GetBytes("uSR");
        msgTurnLeft = Encoding.UTF8.GetBytes("dSR");
        msgTurnStop = Encoding.UTF8.GetBytes("sSR");

        msgOpenClaw = Encoding.UTF8.GetBytes("uSP");
        msgCloseClaw = Encoding.UTF8.GetBytes("dSP");
        msgIdleClaw = Encoding.UTF8.GetBytes("sSP");


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

        Debug.Log("Left joystick values: " + LeftJoystickValue);

        Debug.Log("Right joystick values: " + RightJoyStickValue);

        //Movement for the first servo, called the "elbow" servo, using the two grips at the front of the controllers (left->up; right->down)
        //When the up grip is pressed
        if (grip1Left.state)
        {
            
            //It is cheked if the servo was not already moving up
            if (!elbowUpFlag)
            {
                //It start moving up
                Debug.Log("moving up");
                ch.BasicPublish("", "ClawServos", null, msgElbowUp);
                elbowUpFlag = true;
            }
        }
        //If the up grip is not pressed
        else if (elbowUpFlag)
        {
            elbowUpFlag = false;

            //It is checked if the down grip is not pressed neither
            if (!elbowDownFlag)
            {
                //If so, the servo is stopped
                ch.BasicPublish("", "ClawServos", null, msgElbowStop);
            }

        }

        // The same occurs when the down grip for moving the servo down
        if (grip1Right.state)
        {
            if (!elbowDownFlag)
            {
                Debug.Log("Going down");
                ch.BasicPublish("", "ClawServos", null, msgElbowDown);
                elbowDownFlag = true;
            }
        }
        else if (elbowDownFlag)
        {
            elbowDownFlag = false;

            if (!elbowUpFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgElbowStop);
            }
        }





        //Movement for the second servo, called the "wrist" servo, using the two grips at the side of the controllers (left->up; right->down)
        if (grip2Left.state)
        {
            if (!wristUpFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgWristUp);
                wristUpFlag = true;
            }
        }
        else if (wristUpFlag)
        {
            wristUpFlag = false;

            if (!wristDownFlag) { ch.BasicPublish("", "ClawServos", null, msgWristStop); }
        }

        if (grip2Right.state)
        {
            if (!wristDownFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgWristDown);
                wristDownFlag = true;
            }
        }
        else if (wristDownFlag)
        {
            wristDownFlag = false;

            if (!wristUpFlag) { ch.BasicPublish("", "ClawServos", null, msgWristStop); }
        }




        //Movement for the spinning servo, using the y and b buttons from the controller
        if (yButton.state)
        {
            if (!turnLeftFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgTurnLeft);
                turnLeftFlag = true;
            }
        }
        else if (turnLeftFlag)
        {
            turnLeftFlag = false;

            if (!turnRightFlag) { ch.BasicPublish("", "ClawServos", null, msgTurnStop); }
        }


        if (bButton.state)
        {
            if (!turnRightFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgTurnRight);
                turnRightFlag = true;
            }
        }
        else if (turnRightFlag)
        {
            turnRightFlag = false;
            if (!turnLeftFlag) { ch.BasicPublish("", "ClawServos", null, msgTurnStop); }
        }




        //Movement for the claw servo, using the x and a buttons from the controllers
        if (xButton.state)
        {
            if (!openClawFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgOpenClaw);
                openClawFlag = true;
            }
        }
        else if (openClawFlag)
        {
            openClawFlag = false;
            if (!closeClawFlag) { ch.BasicPublish("", "ClawServos", null, msgIdleClaw); }
        }


        if (aButton.state)
        {
            if (!closeClawFlag)
            {
                ch.BasicPublish("", "ClawServos", null, msgCloseClaw);
                closeClawFlag = true;
            }
        }
        else if (closeClawFlag)
        {
            closeClawFlag = false;
            if (!openClawFlag) { ch.BasicPublish("", "ClawServos", null, msgIdleClaw); }
        }
    }

    private void OnApplicationQuit()
    {
        //When exiting the app, all movements are stopped
        ch.BasicPublish("", "ClawServos", null, msgElbowStop);
        ch.BasicPublish("", "ClawServos", null, msgWristStop);
        ch.BasicPublish("", "ClawServos", null, msgTurnStop);
        ch.BasicPublish("", "ClawServos", null, msgIdleClaw);

        //The queue is purged, in order to not let any unaknowledge message waiting for the next time the robot connects to it.
        ch.QueuePurge("ClawServos");
        ch.Close();

    }
}