import React, { useState } from "react";
import axios from "axios";
import { Input, Button, Typography, FormLabel, Alert} from "@mui/joy";
import Diversity2Icon from '@mui/icons-material/Diversity2';
import { blue } from "@mui/material/colors";
import loginImage from '../Assets/Images/loginImage.avif'
import { Link } from "react-router";
import '../Assets/Styles/login.css'
import Footer from "./footer.jsx";

const Login =({setUserData}) => {
 
    const [formValues, setFormValues] = useState({
        username:  "",
        password: "" 
    });

    const [Alert, setAlert] = useState(false)
    
    
    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormValues({ ...formValues, [name]: value });
    };

    const handleLogin = async (event) => {
        event.preventDefault();

        try{
            const response = await axios.post('http://127.0.0.1:1008/api/login', {
                 username: formValues.username, 
                 password: formValues.password
            });

            if(response.status === 200){
                alert('Inicio de sesión exitoso');
                setUserData(response.data.data);
            }else{
                alert('Credenciales incorrectas')
            }

        }catch (error){
            alert(error.response?.data?.message || "Error al conectar al servidor")
        }
    }

    return(
        <div className="main">
            <div className="container">
                <div className="form">
                    <div className="loginForm">
                        <div className="logo">
                            <Diversity2Icon sx={{color: blue[900]}}/>
                            <Typography textColor={blue[900]}>AlumniUG</Typography>
                        </div>
                        <form onSubmit={handleLogin}>
                            <Typography level='h2' align='center'>Inicio de Sesión</Typography>
                                <FormLabel>Usuario</FormLabel>
                                <Input variant = 'soft'
                                    placeholder="alumnoug@example.com"
                                    type = 'email'
                                    name = 'username'
                                    required
                                    value={formValues.username}
                                    onChange={handleChange}
                                    style = {{marginBottom: '15px'}}
                                />
                                <FormLabel>Contraseña</FormLabel>
                                <Input variant = 'soft'
                                    placeholder="********"
                                    type="password"
                                    name = 'password'
                                    required
                                    value={formValues.password}
                                    onChange={handleChange}
                                />
                                <Typography level= 'body-xs' style={{marginTop : '15px', marginBottom: '20px'}}>
                                    <Link to={'/register'} style={{color: 'black'}}>No tienes cuenta? Registrate!</Link>
                                </Typography>                       
                            <Button variant="solid" color="primary" type="submit" fullWidth>
                                Iniciar Sesión
                            </Button>
                        </form>
                    </div>
                <div className="imageContainer">
                    <img src= {loginImage} alt="" />
                </div>
            </div>
        </div>
        <Footer></Footer>
        </div>
    )
} 

export default Login;