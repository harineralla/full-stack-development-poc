import React, { useState, useEffect } from 'react';
import { Form, Button, Input } from 'antd';
import axios from "axios";
import '../App.css';

export const LOCAL_HOST = 'http://127.0.0.1:5000'

function UserForm() {
    const onFinish = (values) => {
        // debugger
        axios.post('http://127.0.0.1:5000/users', {
            "First Name": values["firstName"],
            "Last Name": values["lastName"],
            "Email": values["email"],
            "Password": values["password"]
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            console.log(response);
        }).catch((error) => {
            console.log("Error posting user details", error)
        })
    };

    return (
        <div className="form-container" >
            <Form
                name="basic"
                initialValues={{
                    remember: true,
                }}
                onFinish={onFinish}
            >
                <Form.Item
                    label="First Name"
                    name="firstName"
                    rules={[
                        {
                            required: true,
                            message: 'Please input your first name!',
                        },
                    ]}
                >
                    <Input />
                </Form.Item>
                <Form.Item
                    label="Last Name"
                    name="lastName"
                    rules={[
                        {
                            required: true,
                            message: 'Please input your last name!',
                        },
                    ]}
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    label="Email"
                    name="email"
                    rules={[
                        {
                            required: true,
                            message: 'Please input your email!',
                        },
                    ]}
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    label="Password"
                    name="password"
                    rules={[
                        {
                            required: true,
                            message: 'Please input your password!',
                        },
                    ]}
                >
                    <Input.Password />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit" onFinish={onFinish}>
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </div>
    );
}

export default UserForm;