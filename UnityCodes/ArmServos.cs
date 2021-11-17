using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RabbitMQ.Client;
using System.Text;



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
        //Movement for the first servo, called the "elbow" servo, using the keys 7(for moving up) and 4(for moving down) from the keypad
        //When the 7 key is pressed
        if (Input.GetKey(KeyCode.Keypad7))
        {
            //It is cheked if the servo was not already moving up
            if (!elbowUpFlag)
            {
                //It start moving up
                ch.BasicPublish("", "ClawServos", null, msgElbowUp);
                elbowUpFlag = true;
            }
        }
        //If the 7 key is not pressed
        else if (elbowUpFlag)
        {
            elbowUpFlag = false;

            //It is checked if the 4 key is not pressed neither
            if (!elbowDownFlag)
            {
                //If so, the servo is stopped
                ch.BasicPublish("", "ClawServos", null, msgElbowStop);
            }

        }

        // The same occurs when the 4 key for moving the servo downn
        if (Input.GetKey(KeyCode.Keypad4))
        {
            if (!elbowDownFlag)
            {
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





        //Movement for the second servo, called the "wrist" servo, using the keys 8(for moving up) and 5(for moving down) from the keypad
        if (Input.GetKey(KeyCode.Keypad8))
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

        if (Input.GetKey(KeyCode.Keypad5))
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




        //Movement for the spinning servo, using the keys 1(for moving left) and 2(for moving right) from the keypad
        if (Input.GetKey(KeyCode.Keypad1))
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


        if (Input.GetKey(KeyCode.Keypad2))
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
            if (!turnLeftFlag){ ch.BasicPublish("", "ClawServos", null, msgTurnStop); }
        }




        //Movement for the claw servo, using the keys 0(for opening) and enter(for closing) from the keypad
        if (Input.GetKey(KeyCode.Keypad0))
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


        if (Input.GetKey(KeyCode.KeypadEnter))
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
