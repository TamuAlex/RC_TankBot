using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RabbitMQ.Client;
using System.Text;

public class ArmServos : MonoBehaviour
{

    bool elbowUpFlag;
    bool elbowDownFlag;
    bool wristUpFlag;
    bool wristDownFlag;
    bool turnLeftFlag;
    bool turnRightFlag;


    byte[] msgElbowUpOn;
    byte[] msgElbowDownOn;
    byte[] msgWristUpOn;
    byte[] msgWristDownOn;
    byte[] msgTurnRightOn;
    byte[] msgTurnLeftOn;

    byte[] msgElbowUpOff;
    byte[] msgElbowDownOff;
    byte[] msgWristUpOff;
    byte[] msgWristDownOff;
    byte[] msgTurnLeftOff;
    byte[] msgTurnRightOff;
    //Declaration of the RabbitMQ channel
    IModel ch;
    IBasicProperties properties;

    // Start is called before the first frame update
    void Start()
    {
        string serverAddress = "amqps://zvaqximc:I2_yD3JdVLcdqBIdH__EUToUUdEVSsWf@fish.rmq.cloudamqp.com/zvaqximc";
         elbowUpFlag = false;
         elbowDownFlag = false;
         wristUpFlag = false;
         wristDownFlag = false;
        turnLeftFlag = false;
        turnRightFlag = false;

        msgElbowUpOn = Encoding.UTF8.GetBytes("elbowUp");
        msgElbowDownOn = Encoding.UTF8.GetBytes("elbowDown");
        msgWristUpOn = Encoding.UTF8.GetBytes("wristUn");
        msgWristDownOn = Encoding.UTF8.GetBytes("wristDown");
        msgTurnRightOn = Encoding.UTF8.GetBytes("right");
        msgTurnLeftOn = Encoding.UTF8.GetBytes("left");

        msgElbowUpOff = Encoding.UTF8.GetBytes("selbowUp");
        msgElbowDownOff = Encoding.UTF8.GetBytes("selbowDown");
        msgWristUpOff = Encoding.UTF8.GetBytes("swristUp");
        msgWristDownOff = Encoding.UTF8.GetBytes("swristDown");
        msgTurnLeftOff = Encoding.UTF8.GetBytes("sleft");
        msgTurnRightOff = Encoding.UTF8.GetBytes("sright");

        ConnectionFactory cf = new ConnectionFactory();
        cf.Uri = serverAddress;
        IConnection conn = cf.CreateConnection();
        ch = conn.CreateModel();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.Keypad7))
        {
            if (elbowUpFlag)
            {
                Debug.Log("Movemos Codo Arriba");
                ch.BasicPublish("", "ClawServos", null, msgElbowUpOn);
                elbowUpFlag = true;
            }
        }
        else if (elbowUpFlag)
        {
            Debug.Log("Paramos codo arriba");
            ch.BasicPublish("", "ClawServos", null, msgElbowUpOff);
            elbowUpFlag = false;

        }

        if (Input.GetKey(KeyCode.Keypad4))
        {
            if (elbowDownFlag)
            {
                Debug.Log("Movemos Codo abajo");
                ch.BasicPublish("", "ClawServos", null, msgElbowDownOn);
                elbowDownFlag = true;
            }
        }
        else if (elbowDownFlag)
        {
            Debug.Log("Paramos Codo abajo");
            ch.BasicPublish("", "ClawServos", null, msgElbowDownOff);
            elbowDownFlag = false;
        }

        if (Input.GetKey(KeyCode.Keypad8))
        {
            if (wristUpFlag)
            {
                Debug.Log("Movemos Muñeca arriba");
                ch.BasicPublish("", "ClawServos", null, msgWristUpOn);
                wristUpFlag = true;
            }
        }
        else if (wristUpFlag)
        {
            Debug.Log("Paramos Muñeca arriba");
            ch.BasicPublish("", "ClawServos", null, msgWristUpOff);
            wristDownFlag = false;
        }

        if (Input.GetKey(KeyCode.Keypad5))
        {
            if (wristDownFlag)
            {
                Debug.Log("Movemos muñeca abajo");
                ch.BasicPublish("", "ClawServos", null, msgWristDownOn);
                wristDownFlag = true;
            }
        }
        else if (wristDownFlag)
        {
            Debug.Log("Paramos muñeca abajo");
            ch.BasicPublish("", "ClawServos", null, msgWristDownOff);
            wristDownFlag = false;
        }


        if (Input.GetKey(KeyCode.Keypad1))
        {
            if (turnLeftFlag)
            {
                Debug.Log("Giramos Izq");
                ch.BasicPublish("", "ClawServos", null, msgTurnLeftOn);
                wristDownFlag = true;
            }
        }
        else if (turnLeftFlag)
        {
            Debug.Log("Paamos Giro Izq");
            ch.BasicPublish("", "ClawServos", null, msgTurnLeftOff);
            wristDownFlag = false;
        }


        if (Input.GetKey(KeyCode.Keypad2))
        {
            if (turnRightFlag)
            {
                Debug.Log("Giramos dcha");
                ch.BasicPublish("", "ClawServos", null, msgTurnRightOn);
                wristDownFlag = true;
            }
        }
        else if (turnRightFlag)
        {
            Debug.Log("Paamos Giro dcha");
            ch.BasicPublish("", "ClawServos", null, msgTurnRightOff);
            wristDownFlag = false;
        }
    }

    private void OnApplicationQuit()
    {
        ch.QueuePurge("ClawServos");
        Debug.Log("ClawServos Purged");
        ch.Close();

    }
}
