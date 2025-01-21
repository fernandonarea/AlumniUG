import React, { useEffect, useState } from "react";
import { Typography, Avatar } from "@mui/joy";
import Navbar from "../Components/navbar";
import axios from "axios";
import '../Assets/Styles/profile.css';

const Profile = ({ userData, setUserData }) => {
    const id_user = userData.user_id;
    const token = userData.token;
    const [post, setPost] = useState([]);
    const [numlikes, setNumLikes] = useState({});
    const [numAmigos, setNumAmigos] = useState(0);

    // Obtener publicaciones del usuario
    const fetchPostUser = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:1011/posts/user/${id_user}`, {
                headers: { token: token }
            });

            if (response.status === 200) {
                setPost(response.data.data);
                if (response.data.data === 500) {
                    alert('No hay publicaciones');
                }
            } else {
                console.error('Error al obtener los post del usuario:', response.data.message);
            }
        } catch (error) {
            console.error('Error al obtener los post del usuario:', error);
        }
    };

    // Obtener el número de amigos
    const numFriends = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:1015/num/friends/${id_user}`, {
                headers: { token: token }
            });

            if (response.status === 200 && response.data.data.length > 0) {
                setNumAmigos(response.data.data[0].total_amigos); // Accedemos a total_amigos dentro del array
            } else {
                console.log('No se obtuvo el número de amigos');
            }
        } catch (error) {
            console.log('Error al obtener el número de amigos:', error);
        }
    };

    const fetchLikes = async () => {
        try {
            const likes = {};
            for (let postItem of post) {
                const response = await axios.get(`http://127.0.0.1:1011/likes/${postItem.id_post}`, {
                    headers: { token: token }
                });

                if (response.status === 200) {
                    likes[postItem.id_post] = response.data.data;
                }
            }
            setNumLikes(likes);
        } catch (error) {
            console.error('Error al obtener los likes de las publicaciones:', error);
        }
    };

    // useEffect para obtener publicaciones, amigos y likes
    useEffect(() => {
        const fetchData = async () => {
            await Promise.all([fetchPostUser(), numFriends()]);
            fetchLikes();
        };

        fetchData();
    }, []);

    return (
        <>
            <Navbar userData={userData} setUserData={setUserData} />
            <div className="parent">
                <div className="profile">
                    <div className="profile-info">
                        <Avatar sx={{ "--Avatar-size": "186px" }}>
                            {userData.name.charAt(0) + userData.lastname.charAt(0)}
                        </Avatar>
                        <Typography fontWeight={'bold'} level='title-lg'>
                            {userData.name} {userData.lastname}
                        </Typography>
                        <Typography level='body-md'>{userData.nombre_facultad}</Typography>
                        <div className="statsProfile">
                            <Typography>Amigos: {numAmigos}</Typography>
                            <Typography>Publicaciones: {post.length}</Typography>
                        </div>
                    </div>
                </div>

                <div className="postUser">
                    {post.map((postItem) => (
                        <div key={postItem.id_post} className="posts">
                            <Typography level="body-xs">{postItem.date}</Typography>
                            <Typography level="body-lg">{postItem.post_content}</Typography>
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
};

export default Profile;
