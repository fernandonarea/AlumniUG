import React from "react";
import Comments from "../Components/comments";

const ListComentarios = ({userData, post}) => {
    
    return(
        <div>
            <Comments post={post} userData={userData}/>
        </div>
    )
}
export default ListComentarios