import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Login from './Components/login';
import Register from './Components/register';
import Main from './Pages/main';
import './Assets/Styles/app.css'
import Profile from "./Pages/profile";
import ListUsers from "./Pages/listUsers";
import ListComentarios from "./Pages/listComentarios";
import Foros from "./Pages/foros";

const App = () => {
  const [userData, setUserData] = useState(null);

  return (
    <>
      <Routes>
        <Route path="/" element={!userData ? <Login setUserData={setUserData} /> : <Main userData={userData} setUserData={setUserData} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/main" element={<Main userData={userData} setUserData={setUserData}/>} />
        <Route path="/profile" element={<Profile userData={userData} setUserData={setUserData} />} />
        <Route path="/users" element={<ListUsers userData={userData} setUserData={setUserData}/>}></Route>
        <Route path="/comments" element={<ListComentarios userData={userData} setUserData={setUserData}/>}></Route>
        <Route path="/foros" element={<Foros userData={userData} setUserData={setUserData}/>}></Route>
      </Routes>
    </>
  );
};

export default App;