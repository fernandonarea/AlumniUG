import React, { useEffect, useState } from "react";
import { Typography, Button, Avatar, Divider, Snackbar, Modal, ModalDialog, DialogTitle, FormControl, FormLabel, Input } from "@mui/joy";
import ThumbUpOutlinedIcon from '@mui/icons-material/ThumbUpOutlined';
import TextsmsOutlinedIcon from '@mui/icons-material/TextsmsOutlined';
import axios from "axios";
import '../Assets/Styles/main.css';
import Comments from "./comments";

const Publicaciones = ({userData}) => {
    const token = userData.token;
    const user_id = userData.user_id;
    
    const [post, setPost] = useState([]);
    const [numLikes, setNumLikes] = useState({});
    const [numsComments, setNumsComments] = useState({}); 
    const [formValues, setFormValues] = useState({
        comment_text: ""
    });
    const [color, setColor] = useState('success');
    const [openSnackbar, setOpenSnackbar] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState('');
    const [openModals, setOpenModals] = useState({});
    const [iconColor, setIconColor] = useState({});
    const [commentsVisible, setCommentsVisible] = useState({});  // Estado para manejar la visibilidad de los comentarios

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormValues({ ...formValues, [name]: value });
    };

    const handleLike = async (id_post) => {
        try {
            const response = await axios.post(`http://127.0.0.1:1013/likes/create/${id_post}/${user_id}`, {}, {
                headers: {
                    token: token
                }
            });

            if (response.status === 200) {
                setOpenSnackbar(true);
                setColor('success');
                setSnackbarMessage('Haz dado like a esta publicación');
                setIconColor((prevColors) => {
                    const updatedColors = { ...prevColors, [id_post]: "success" };
                    localStorage.setItem('likeIcons', JSON.stringify(updatedColors));
                    return updatedColors;
                });
            } else {
                setSnackbarMessage('Esta publicación ya tiene un like tuyo');
                setOpenSnackbar(true);
                console.error('Error en la respuesta del servidor:', response.data.message);
            }

        } catch (error) {
            setOpenSnackbar(true);
            setColor('danger');
            setSnackbarMessage('Esta publicación ya tiene un like tuyo');
        }
    };

    const handleComment = async (event, post_id) => { 
        event.preventDefault();
        try {
            const response = await axios.post(`http://127.0.0.1:1013/comments/create/${user_id}/${post_id}`, 
            { comment_text: formValues.comment_text }, 
            { headers: { token: token } });

            if(response.status === 200){
                console.log('Comentario creado correctamente');
                setSnackbarMessage('Comentario creado correctamente');
                setColor('success');
                setOpenSnackbar(true);
            } else {
                console.error('Error en la respuesta del servidor:', response.data.message);
                setSnackbarMessage('Error al crear el comentario');
                setColor('danger');
                setOpenSnackbar(true);
            }
        } catch (error) {
            console.error('Error al crear comentario:', error);
            setSnackbarMessage('Error al crear el comentario');
            setColor('danger');
            setOpenSnackbar(true);
        }
    };

    const fetchPosts = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:1011/posts', {
                headers: { Authorization: `Bearer ${token}` },
            });

            if (response.status === 200) {
                setPost(response.data.data);

                const savedColors = localStorage.getItem('likeIcons');
                if (savedColors) {
                    setIconColor(JSON.parse(savedColors));
                }

                const fetchedLikes = {};  
                const fetchedComments = {};  
                response.data.data.forEach((postItem) => {
                    fetchedLikes[postItem.id_post] = postItem.total_likes;
                    fetchedComments[postItem.id_post] = postItem.total_comments;
                });
                setNumLikes(fetchedLikes);
                setNumsComments(fetchedComments);
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

    const toggleCommentsVisibility = (id_post) => {
        setCommentsVisible((prevState) => ({
            ...prevState,
            [id_post]: !prevState[id_post]
        }));
    };

    return (
        <>
            {post.map((postItem) => (
                <div key={postItem.id_post} className="post">
                    <div className="post-head">
                        <Avatar>{postItem.owner_name.charAt(0) + postItem.owner_lastname.charAt(0)}</Avatar>
                        <Typography level="body-lg" fontWeight={'bold'}>
                            {postItem.owner_name + " " + postItem.owner_lastname}
                        </Typography>
                        <Typography level="body-xs">{postItem.date}</Typography>
                    </div>
                    <div className="post-content">
                        <Typography level="body-lg">{postItem.post_content}</Typography>
                    </div>
                    <Divider />
                    <div className="interactions">
                        <Button 
                            variant="plain"  
                            onClick={() => handleLike(postItem.id_post)}
                            color={iconColor[postItem.id_post]}
                            fullWidth
                        >
                            <ThumbUpOutlinedIcon /> 
                            <Typography>{numLikes[postItem.id_post]}</Typography>
                        </Button>
                        
                        <Button 
                            variant="plain" 
                            onClick={() => setOpenModals({ ...openModals, [postItem.id_post]: true })}
                            fullWidth
                        >
                            <TextsmsOutlinedIcon />
                        </Button>

                        <Button 
                            variant="outlined" 
                            onClick={() => toggleCommentsVisibility(postItem.id_post)} // Alternar visibilidad de comentarios
                            fullWidth
                        >
                            {commentsVisible[postItem.id_post] ? "Ocultar comentarios" : "Mostrar comentarios"}
                        </Button>

                        <Modal 
                            open={openModals[postItem.id_post] || false} 
                            onClose={() => setOpenModals({ ...openModals, [postItem.id_post]: false })}
                        >
                            <ModalDialog color="primary">
                                <DialogTitle>Nuevo comentario</DialogTitle>
                                <form onSubmit={(event) => handleComment(event, postItem.id_post)} className="newComment">
                                    <FormControl>
                                        <FormLabel>Comentario</FormLabel>
                                        <Input 
                                            type="text" 
                                            name="comment_text" 
                                            value={formValues.comment_text}
                                            onChange={handleChange} 
                                        />
                                        <div className="btnComments">
                                            <Button variant="solid" color="primary" type="submit">
                                                Comentar
                                            </Button>
                                            <Button variant="outlined">Ver comentarios</Button>
                                        </div>
                                    </FormControl>
                                </form>
                            </ModalDialog>
                        </Modal>
                    </div>

                    {commentsVisible[postItem.id_post] && <Comments post={postItem} userData={token} />}
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
        </>
    );
}

export default Publicaciones;