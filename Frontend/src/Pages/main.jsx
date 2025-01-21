import React, { useEffect, useState } from "react";
import ShowChartIcon from '@mui/icons-material/ShowChart';
import { Button,  Divider, Typography, Input, Snackbar } from "@mui/joy";
import Navbar from "../Components/navbar";
import Publicaciones from "../Components/publicaciones";
import Stats from "../Components/stats";
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import { Navigate, useNavigate } from "react-router-dom";
import '../Assets/Styles/main.css';
import axios from "axios";

const Main = ({ userData, setUserData }) => {
  
    const [post, setPost] = useState([]);
    const[color, setColor] = useState('success');
    const [newPost, setNewPost] = useState({'post_content': ''})
    const [openSnackbar, setOpenSnackbar] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState('');
    
    const token = userData.token
    const user_id = userData.user_id
    
    const navigate = useNavigate();
    
    const handleNavigation = () => {
      navigate("/users");
    };

    const handleNavigation2 = () => {
      navigate("/foros");
    };
    
    const handleChange = (event) => {
        const { name, value } = event.target;
        setNewPost({ ...newPost, [name]: value });
    };
    
    const HandlenewPost = async (event) => {
        event.preventDefault();
        
        try {
          const response = await axios.post(`http://127.0.0.1:1011/posts/create/${user_id}`, 
          {
            post_content: newPost.post_content,
          },
          {
            headers:
            {
                token: token
            },
          }
        );
    
          if (response.status === 200) {
            console.log('Post creado correctamente');
            setSnackbarMessage('Post Creado con exito');
            setColor('success');
            setOpenSnackbar(true)
            fetchPosts();
          } else {
            console.error('Error en la respuesta del servidor:', response.data.message);
            setSnackbarMessage('Error al crear el post');
            setColor('danger');
            setOpenSnackbar(true)
          }
        } catch (error) {
          console.error('Error al crear post:', error);
          setSnackbarMessage('Error al crear el post');
          setColor('danger');
          setOpenSnackbar(true)
        }
    };
    

    const fetchPosts = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:1011/posts', {
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            });

            if (response.status === 200) {
                setPost(response.data.data);
            } else {
                console.error("Error en la respuesta del servidor:", response.data.message);
            }
        } catch (error) {
            console.error("Error al obtener posts:", error);
        }
    };

    useEffect(() => {
        fetchPosts();
    }, []);

    return (
    <div>
    <Navbar userData={userData} setUserData={setUserData}/>
      <div className="content">
        <div className="content-center">
            <div className="post">
                <div className="newpost">
                    <form onSubmit={HandlenewPost} className="newpost-form">
                        <Input
                            type="text"
                            name="post_content"
                            placeholder="Escribe tu post"
                            value={newPost.post_content}
                            onChange={handleChange}
                        />
                        <Button variant="solid" color="primary" type="submit" onClick={fetchPosts}>
                            Publicar
                        </Button>
                        <Snackbar
                            open={openSnackbar}
                            variant="soft"
                            autoHideDuration={3000}
                            color={color}
                            onClose={() => setOpenSnackbar(false)}
                        >
                            {snackbarMessage}
                        </Snackbar>
                    </form>
                </div>
            </div>
            <Divider></Divider>
            
            <Publicaciones userData={userData} setUserData={setUserData}/>
            
            <Divider></Divider>
        </div>

        <div className="content-rigth">
            <div className="stats">
              <div className="ttl">
                <ShowChartIcon />
                <Typography level="h4" textColor="white">Estadisticas</Typography>
              </div>
              <Stats userData={userData} setUserData={setUserData}/>
            </div>
            <div className="btnsActions">
              <Button onClick={handleNavigation} startDecorator= {<PersonAddIcon/>}>Buscar Amigos</Button>
              <Button onClick={handleNavigation2}>Foros</Button>
            </div>
          </div>
        </div>
      </div>
    );
};

export default Main;
