import React, { useEffect, useState } from "react";
import axios from "axios";
import { Snackbar, Button, Typography, Input } from "@mui/joy";
import "../Assets/Styles/listUsers.css";

const Friends = ({userData}) => {
    
    const token = userData.token;
    const user_id = userData.user_id

    const [openSnackbar, setOpenSnackbar] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState("");
    const [color, setColor] = useState("success");
    const [btncolor, setBtnColor] = useState({});
    const [users, setUsers] = useState([]);
    const [searchTerm, setSearchTerm] = useState("");

    const fetchUsers = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:1009/api/users/${user_id}`, {
                headers: {
                    token: token,
                },
            });

            if (response.status === 200) {
                setUsers(response.data.data);
            } else {
                console.log("No se obtuvieron los usuarios");
            }
        } catch (error) {
            console.log("Error en el fetch de usuarios");
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    const addFriend = async (amigo_id) => {
        try {
            const response = await axios.post(
                `http://127.0.0.1:1015/add/friend/${user_id}/${amigo_id}`,
                {},
                {
                    headers: {
                        token: token,
                    },
                }
            );

            if (response.status === 201) {
                console.log("Amigo agregado con éxito");
                setOpenSnackbar(true);
                setColor("success");
                setSnackbarMessage("Amigo agregado con éxito");

                setBtnColor((prevColors) => ({
                    ...prevColors,
                    [amigo_id]: "success",
                }));

            } else {
                setOpenSnackbar(true);
                setColor("danger");
                setSnackbarMessage("No se pudo añadir a la lista de amigos");
            }
        } catch (error) {
            console.log("Error en el servicio de agregar amigos");
            setOpenSnackbar(true);
            setColor("danger");
            setSnackbarMessage("No se pudo añadir a la lista de amigos");
        }
    };

    const filteredUsers = users.filter(
        (user) =>
            user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.username.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.lastname.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <>
            <div className="busqueda">
                <div className="input">
                    <Input
                        type="text"
                        placeholder="Buscar amigos por nombre o username"
                        variant='soft'
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        className="search-bar"
                    />
                </div>
            </div>
            <div className="usuarios">
                {filteredUsers.map((user) => (
                    <div key={user.id_user} className="users-list">
                        <Typography level="body-lg" fontWeight="bold">
                            {user.name} {user.lastname}
                        </Typography>
                        <Typography level="body-xs">{user.username}</Typography>
                        <Button 
                            onClick={() => addFriend(user.id_user)} 
                            color={btncolor[user.id_user]} 
                        >
                            Añadir a lista de amigos
                        </Button>
                    </div>
                ))}
                <Snackbar
                    open={openSnackbar}
                    variant="soft"
                    autoHideDuration={2000}
                    color={color}
                    onClose={() => setOpenSnackbar(false)}
                >
                    {snackbarMessage}
                </Snackbar>
            </div>
        </>
    );
};

export default Friends;
