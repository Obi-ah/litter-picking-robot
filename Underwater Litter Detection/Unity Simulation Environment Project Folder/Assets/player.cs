using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player : MonoBehaviour
{
    public float speed = 0.5f; // 移动速度
    public float rotationSpeed = 15.0f; // 旋转速度
    public float verticalSpeed = 0.5f; // 上升和下降的速度

    // Update is called once per frame
    void Update()
    {
        Vector3 movement = Vector3.zero;
        
        // 水平和前后移动
        if (Input.GetKey(KeyCode.J)) // 向左移动
        {
            movement.x = -1;
        }
        else if (Input.GetKey(KeyCode.L)) // 向右移动
        {
            movement.x = 1;
        }

        if (Input.GetKey(KeyCode.I)) // 向前移动
        {
            movement.z = 1;
        }
        else if (Input.GetKey(KeyCode.K)) // 向后移动
        {
            movement.z = -1;
        }

        // 上升和下降
        if (Input.GetKey(KeyCode.N)) // 上升
        {
            movement.y = 1;
        }
        else if (Input.GetKey(KeyCode.M)) // 下降
        {
            movement.y = -1;
        }

        transform.Translate(movement * speed * Time.deltaTime, Space.World);
        
        // 旋转控制
        if (Input.GetKey(KeyCode.U)) // 逆时针旋转
        {
            transform.Rotate(Vector3.up, -rotationSpeed * Time.deltaTime);
        }
        else if (Input.GetKey(KeyCode.O)) // 顺时针旋转
        {
            transform.Rotate(Vector3.up, rotationSpeed * Time.deltaTime);
        }
    }
}

