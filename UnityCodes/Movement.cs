using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RabbitMQ.Client;
using System.Text;


/************************************************************
 *                                                          *
 *                      Authors:                            *
 *   Alejandro Ortega Martinez: alejandro.ormar@gmail.com   *
 *   Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es          *
 *                                                          *
 ***********************************************************/

/************************************************************
 * Script to connect the movement of the raspberry Pi to   *
 * the Unity project using the AMQP protocol, the           *
 * RabbitMQ library, and hosting the broker in              *
 * cloudamp.com                                             *
 ************************************************************/

public class Movement : MonoBehaviour
{
    //Declaration of flags for only sending a message per movement, not one per frame, for not flooding the queue
    bool fFlag;
    bool bFlag;
    bool lFlag;
    bool rFlag;
    bool stopFlag;

    //Declaration of the different messages that we can send to the robot
    byte[] messageFwrd;
    byte[] messageBwrd;
    byte[] messageLeft;
    byte[] messageRight;
    byte[] messageStop;

    //Declaration of the RabbitMQ channel
    IModel ch;
    IBasicProperties properties;

    // Start is called before the first frame update
    void Start()
    {
        //Declaring the amqp server Address
        string serverAddress = "amqps://zvaqximc:I2_yD3JdVLcdqBIdH__EUToUUdEVSsWf@fish.rmq.cloudamqp.com/zvaqximc"; 

        //The different messages that can be sent, encoded in a byte stream
        messageFwrd = Encoding.UTF8.GetBytes("forward");
        messageBwrd = Encoding.UTF8.GetBytes("back");
        messageLeft = Encoding.UTF8.GetBytes("left");
        messageRight = Encoding.UTF8.GetBytes("right");
        messageStop = Encoding.UTF8.GetBytes("stop");


        //Establish the connection to the AMQP server
        ConnectionFactory cf = new ConnectionFactory();
        cf.Uri = serverAddress;
        IConnection conn = cf.CreateConnection();
        ch = conn.CreateModel();
        properties = ch.CreateBasicProperties();
        properties.Expiration = "100";

        //Initialize the flags according to the movement of the robot at the start of the script (stopped)
        fFlag = false; 
        bFlag = false; 
        lFlag = false; 
        rFlag = false;
        stopFlag = true;

    }

    // Update is called once per frame
    void Update()
    {
        // Forwrd movement, pressing the "w" key
        //If the w key is pressed
        if (Input.GetKey("w"))
        {
            //check that we were not already moving forward
            if (!fFlag)
            {
                //The flag is set to True to let next frames know that the robot is moving forward
                fFlag = true;
                //A message is sent to the broker
                ch.BasicPublish("", "movement", null, messageFwrd);

                //The stop flag is checked to see if the robot was stopped. If so, the stop flag is set to True to let the script know that
                //when no key is pressed, it has to enter in the "stop" if.
                if (!stopFlag)
                {
                    stopFlag = true;
                }
            }
        }
        else
        {
            //If it was previously moving forward, and now is stopped, we mark the forward flag as false, to know that it is not moving forward
            if (fFlag) { fFlag = false; }
        }




        // Backward movement, pressing the "s" key
        if (Input.GetKey("s"))
        {
            if (!bFlag)
            {
                bFlag = true;
                ch.BasicPublish("", "movement", null, messageBwrd);

                if (!stopFlag)
                {
                    stopFlag = true;
                }
            }
        }
        else
        {
            if (bFlag) { bFlag = false; }
        }




        // Left movement, pressing the "a" key
        if (Input.GetKey("a"))
        {
            if (!lFlag)
            {
                lFlag = true;
                ch.BasicPublish("", "movement", null, messageLeft);

                if (!stopFlag)
                {
                    stopFlag = true;
                }
            }
        }
        else
        {
            if (lFlag) { lFlag = false; }
        }




        // Right movement, pressing thee "d" key
        if (Input.GetKey("d"))
        {
            if (!rFlag)
            {
                rFlag = true;
                ch.BasicPublish("", "movement", null, messageRight);

                if (!stopFlag)
                {
                    stopFlag = true;
                }
            }
        }
        else
        {
            if (rFlag) { rFlag = false; }
        }



        //If no movement key is pressed, the stop flag is checked to know if the robot was moving and it need to stop
        if (!fFlag && !bFlag && !lFlag && !rFlag)
            {
            if (stopFlag)
            {
                stopFlag = false;
                ch.BasicPublish("", "movement", null, messageStop);
            }
         }

        
    }


    private void OnApplicationQuit()
    {
        //When exiting the app, all movements are stopped
        ch.BasicPublish("", "movement", null, messageStop);
        //The queue is purged, in order to not let any unaknowledge message waiting for the next time the robot connects to it.
        ch.QueuePurge("movement");
        ch.Close();
    }
}
