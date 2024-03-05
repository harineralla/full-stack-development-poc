import { useState } from 'react';
import axios from "axios";


export const getData = () => {
    return axios({
        method: "GET",
        url: "/profile",
    })
        .then((response) => {
            const res = response.data
            setProfileData(({
                profile_name: res.name,
                about_me: res.about
            }))
        }).catch((error) => {
            if (error.response) {
                console.log(error.response)
                console.log(error.response.status)
                console.log(error.response.headers)
            }
        })
}