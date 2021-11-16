using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RabbitMQ.Client;
using System.Text;

public class CameraServo : MonoBehaviour
{

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

        upFlag = false;
        downFlag = false;
        leftFlag = false;
        rightFlag = false;

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
        if (Input.GetKey(KeyCode.UpArrow))
        {
            if (!upFlag)
            {
                Debug.Log("Movemos Arriba");
                ch.BasicPublish("", "CameraServos", null, msgUpOn);
                upFlag = true;
            }
        } else if (upFlag) 
        {   Debug.Log("Paramos arriba");
            ch.BasicPublish("", "CameraServos", null, msgUpOff);
            upFlag = false; 

        }

        if (Input.GetKey(KeyCode.DownArrow))
        {
            if (!downFlag)
            {
                Debug.Log("Movemos abajo");
                ch.BasicPublish("", "CameraServos", null, msgDwnOn);
                downFlag = true;
            }
        } else if (downFlag) 
        { 
            Debug.Log("Paramos abajo");
            ch.BasicPublish("", "CameraServos", null, msgDwnOff);
            downFlag = false; 
        }

        if (Input.GetKey(KeyCode.LeftArrow))
        {
            if (!leftFlag)
            {
                Debug.Log("Movemos izquierda");
                ch.BasicPublish("", "CameraServos", null, msgLftOn);
                leftFlag = true;
            }
        } else if (leftFlag) { 
            Debug.Log("Paramos izq");
            ch.BasicPublish("", "CameraServos", null, msgLftOff);
            leftFlag = false; 
        }

        if (Input.GetKey(KeyCode.RightArrow))
        {
            if (!rightFlag)
            {
                Debug.Log("Movemos derecha");
                ch.BasicPublish("", "CameraServos", null, msgRgthOn);
                rightFlag = true;
            }
        } else if (rightFlag) { 
            Debug.Log("Paramos dcha");
            ch.BasicPublish("", "CameraServos", null, msgRghtOff);
            rightFlag = false; 
        }
    }

    private void OnApplicationQuit()
    {
        ch.QueuePurge("CameraServos");
        Debug.Log("CameraServos Purged");
        ch.Close();
        
    }
}
