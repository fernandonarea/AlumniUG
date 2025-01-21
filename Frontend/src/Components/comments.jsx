import React, { useEffect, useState } from "react";
import axios from "axios";
import { Typography, Avatar, containerClasses } from "@mui/joy";
import '../Assets/Styles/comments.css'

const Comments = ({post, userData}) =>{

    const post_id = post.id_post
    const token = userData
    const [comments, setComments] = useState([])

    const fetchComments = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:1013/comments/${post_id}`, {
                headers : {
                    token : token
                }
            })
    
            if(response.status === 200){
                setComments(response.data.data)
                console.log('Comentarios obtenidos con exito')
            }else{
                console.log('no se obtuvieron resultados')
            }
        } catch (error) {
            console.log('ERROR')
        }

    }
    
    useEffect(() => {
        fetchComments();
    }, []);



    return(
        <div class="comment-containerClasses">
            {comments.map((comment)=>(
                <div key={comment.user_id}>
                    <div className="comment-section">
                        <div className="owner">
                            <Avatar>{comment.owner_name.charAt(0)}{comment.owner_last_name.charAt(0)}</Avatar>
                            <Typography level='body-lg'>{comment.owner_name} {comment.owner_last_name}</Typography>
                        </div>
                        <div className="comment">
                            <Typography level='body-xs'>{comment.text}</Typography>
                        </div>
                    </div>
                </div>
            ))}
        
        </div>
    )
}

export default Comments