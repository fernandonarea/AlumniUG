import React from "react";
import Friends from "../Components/friends";
import Navbar from "../Components/navbar";



const ListUsers = ({userData, setUserData}) =>{
    return(
        <>  
            <Navbar userData={userData} setUserData={setUserData}/>
            <Friends userData={userData} setUserData={setUserData}/>
        </>
    )
}

export default ListUsers;