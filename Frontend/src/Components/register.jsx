import React, { useState, useEffect } from "react";
import { Button, FormLabel, Input, Typography, Select, Option, Alert } from "@mui/joy";
import Diversity2Icon from '@mui/icons-material/Diversity2';
import { blue } from "@mui/material/colors";
import { Link } from "react-router-dom";
import '../Assets/Styles/register.css';
import Footer from "./footer";

const RegisterUser = () => {
    const [formValues, setFormValues] = useState({
        username: "",
        password: "",
        name: "",
        lastname: "",
        id_facultad: "",
    });


    const [facultades, setFacultades] = useState([]);

    const fetchFacultades = async () => {
        try {
            const response = await fetch("http://127.0.0.1:1012/facultades");
            const data = await response.json();

            if (data.result && data.data) {
                setFacultades(data.data);
            } else {
                console.error("Error en la respuesta del servidor:", data.message);
                setFacultades([]);
            }
        } catch (error) {
            console.error("Error al obtener facultades:", error);
            setFacultades([]);
        }
    };

    useEffect(() => {
        fetchFacultades();
    }, []);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormValues({ ...formValues, [name]: value });
    };

    const handleRegister = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch("http://127.0.0.1:1009/api/users", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formValues),
            });

            const data = await response.json();

            if (response.ok) {
                alert("Usuario registrado correctamente");
                setFormValues({
                    username: "",
                    password: "",
                    name: "",
                    lastname: "",
                    id_facultad: "",
                });
            } else {
                alert(data.message || "Error al registrar usuario");
            }
        } catch (error) {
            alert("Ocurrió un error al conectar con el servicio");
            console.error(error);
        }
    };

    return (
        <div className="register-container">
            <div className="logo-registro">
                <Diversity2Icon fontSize="large" sx={{ color: blue[900] }} />
                <Typography level="h3" color="black" textColor={blue[900]}>
                    AlumniUG
                </Typography>
            </div>
            <div className="formRegister">
                <Typography level="h2" align="center" marginBottom="36px">
                    Registro de Usuario
                </Typography>
                <form onSubmit={handleRegister}>
                    <div className="container-form">
                        <div className="namesInputs">
                            <FormLabel>Nombre</FormLabel>
                            <Input
                                variant="soft"
                                placeholder="Ingresa tu nombre"
                                type="text"
                                name="name"
                                value={formValues.name}
                                onChange={handleChange}
                                required
                            />
                            <FormLabel>Apellido</FormLabel>
                            <Input
                                variant="soft"
                                placeholder="Ingresa tu apellido"
                                type="text"
                                name="lastname"
                                value={formValues.lastname}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <FormLabel>Correo Electrónico</FormLabel>
                        <Input
                            variant="soft"
                            placeholder="Ingresa tu correo electrónico"
                            type="email"
                            name="username"
                            value={formValues.username}
                            onChange={handleChange}
                            required
                        />
                        <FormLabel>Facultad</FormLabel>
                        <Select
                            name="id_facultad"
                            value={formValues.id_facultad}
                            onChange={(event, value) =>
                                setFormValues({ ...formValues, id_facultad: value })
                            }
                            placeholder="Seleccione una facultad"
                            required
                        >
                            {facultades.map((facultad) => (
                                <Option key={facultad.id_facultad} value={facultad.id_facultad}>
                                    {facultad.nombre}
                                </Option>
                            ))}
                        </Select>
                        <FormLabel>Contraseña</FormLabel>
                        <Input
                            variant="soft"
                            placeholder="Crea Contraseña"
                            type="password"
                            name="password"
                            value={formValues.password}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="botones">
                        <Button type="submit" variant="solid" color="primary" fullWidth>
                            Registrarse
                        </Button>
                        <Button variant="solid" color="neutral"  fullWidth>
                            <Link to={'/'}>Cancelar</Link>
                        </Button>
                    </div>
                </form>
            </div>
            <Footer />
        </div>
    );
};

export default RegisterUser;
