import React, { useEffect, useState } from "react";
import axios from "axios";
import { Typography } from "@mui/joy";
import ThumbUpOffAltOutlinedIcon from '@mui/icons-material/ThumbUpOffAltOutlined';
import ForumOutlinedIcon from '@mui/icons-material/ForumOutlined';

const Stats = ({ userData }) => {
    const token = userData.token;
    const user_id = userData.user_id;

    const [bestPost, setBestPost] = useState({});

    const getBestPost = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:1011/posts/best/${user_id}`, {
                headers: {
                    token: token,
                },
            });

            if (response.status === 200) {
                const bestPostData = response.data.data[0];
                setBestPost(bestPostData);
            } else {
                console.log('Error al obtener el mejor stats');
            }
        } catch (error) {
            console.log('Error en la API', error);
        }
    };

    useEffect(() => {
        getBestPost();
    }, [user_id, token]);

    console.log(bestPost);

    return (
        <div className="userStats">
            {bestPost.total_likes && bestPost.total_comments ? (
                <div key={bestPost.total_likes}>
                    <Typography variant="body1" fontWeight={'bold'}>
                        <ThumbUpOffAltOutlinedIcon/>   Likes: {bestPost.total_likes}
                    </Typography>
                    
                    <Typography variant="body1" fontWeight={'bold'}>
                        <ForumOutlinedIcon/>Comments: {bestPost.total_comments}
                    </Typography>
                </div>
            ) : (
                <Typography>No se han encontrado estadísticas para este usuario.</Typography>
            )}
        </div>
    );
};

export default Stats;
