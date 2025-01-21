import React from "react";
import Diversity2Icon from "@mui/icons-material/Diversity2";
import {  MenuItem, MenuButton, Menu, Dropdown, Typography, Avatar} from "@mui/joy";
import { Link, useNavigate } from "react-router-dom";
import { blue } from "@mui/material/colors";
import "../Assets/Styles/navbar.css";

const Navbar = ({ userData, setUserData }) => {
    const navigate = useNavigate();

    const handleLogout = () => {
        setUserData(null); 
        localStorage.clear();
        navigate('/');
    };

    const handleProfile = () => {
        navigate('/profile');
    }

    return (
        <div className="navbar">
            <div className="navbar-left">
                <div className="icon">
                    <Link to={'/main'}><Diversity2Icon fontSize="large" sx={{ color: blue[900] }} /></Link>
                </div>
                <div className="nombreUser">
                    {userData ? (
                        <>
                            <Typography fontWeight={'bold'}>
                                Bienvenido {userData.name} {userData.lastname}
                            </Typography>
                        </>
                    ) : (
                        <Typography>AlumniUG</Typography>
                    )}
                </div>
                
            </div>

            <div className="navbar-right">
                <div className="user-avatar">
                    <Dropdown>
                        <MenuButton sx={{border: 'none'}}>
                        <Avatar>{userData?.name?.charAt(0)}{userData?.lastname?.charAt(0)}</Avatar>
                        </MenuButton>
                        <Menu>
                            <MenuItem onClick={handleProfile}>Perfil</MenuItem>
                            <MenuItem onClick={handleLogout}>Cerrar Sesión</MenuItem>
                        </Menu>
                    </Dropdown>
                </div>
            </div>
        </div>
    );
};

export default Navbar;
