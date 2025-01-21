import React, { useState, useEffect } from "react";
import { Button, Input, Textarea, Typography, Modal, ModalDialog, DialogTitle, DialogContent, Avatar } from "@mui/joy";
import Navbar from "../Components/navbar";
import "../Assets/Styles/foros.css";
import axios from "axios";

const Foros = ({ userData, setUserData }) => {
  const [foros, setForos] = useState([]);
  const [selectedForo, setSelectedForo] = useState(null);
  const [formValues, setFormValues] = useState({
    forum_title: "",
    forum_description: "",
  });
  const [isCreatingForo, setIsCreatingForo] = useState(false);
  const [message, setMessage] = useState({
    message_content: "",
  });

  const token = userData.token;
  const user_id = userData.user_id;

  const fetchForos = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:1016/foros", {
        headers: { token: token },
      });

      if (response.status === 200) {
        setForos(response.data.data);
      } else {
        console.log("No se obtuvieron los foros");
      }
    } catch (error) {
      console.log("Error al obtener los foros", error);
    }
  };

  const getForo = async (id_forum) => {
    try {
      const response = await axios.get(`http://127.0.0.1:1016/foro/${id_forum}`, {
        headers: { token },
      });
  
      if (response.status === 200) {
        const foro = response.data.data[0];
        foro.messages = response.data.data.filter(msg => msg.id_forum === foro.id_forum);
        setSelectedForo(foro);
      } else {
        console.log("No se obtuvo el foro");
      }
    } catch (error) {
      console.log("Error al obtener el foro", error);
    }
  };

  const createForo = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:1016/foros/create",
        {
          forum_title: formValues.forum_title,
          forum_description: formValues.forum_description,
        },
        { headers: { token } }
      );

      if (response.status === 201) {
        fetchForos();
        setIsCreatingForo(false);
        setFormValues({ forum_title: "", forum_description: "" });
      } else {
        console.log("No se pudo crear el foro");
      }
    } catch (error) {
      console.log("Error al crear el foro", error);
    }
  };

  const sendMessage = async () => {
    try {
      const response = await axios.post(`http://127.0.0.1:1016/addMessage/${selectedForo.id_forum}/${user_id}`,
        {
          message_content: message.message_content,
        },
        {
          headers: {
            token: token,
          },
        }
      );

      if (response.status === 201) {
        setMessage({ message_content: "" });
        getForo(selectedForo.id_forum);
      } else {
        console.log("No se pudo enviar el mensaje");
      }
    } catch (error) {
      console.error("Error al enviar el mensaje", error);
    }
  };

  useEffect(() => {
    fetchForos();
  }, []);

  return (
    <div className="mainForos">
      <Navbar userData={userData} setUserData={setUserData} />
      <div className="forosContainer">
        <div className="forosHead">
          <Typography level="h2">Foros de la comunidad</Typography>
          <div className="createForo">
            <Button onClick={() => setIsCreatingForo(true)}>Crear Foro</Button>
          </div>
          <div className="foros">
            {foros.map((foro) => (
              <Button
                variant='outlined'
                key={foro.id_forum}
                className="foroItem"
                onClick={() => getForo(foro.id_forum)}
              >
                {foro.forum_title}
              </Button>
            ))}
          </div>
        </div>

        <Modal open={isCreatingForo} onClose={() => setIsCreatingForo(false)}>
          <ModalDialog>
            <DialogTitle>Nuevo Foro</DialogTitle>
              <form onSubmit={createForo}>
                <Input
                  label="Título"
                  value={formValues.forum_title}
                  onChange={(e) =>
                    setFormValues({ ...formValues, forum_title: e.target.value })
                  }
                />
                <Textarea
                  label="Descripción"
                  value={formValues.forum_description}
                  onChange={(e) =>
                    setFormValues({ ...formValues, forum_description: e.target.value })
                  }
                  sx={{marginTop: '20px'}}
                />
                <div className="btnForm">
                  <Button type="submit">Crear Foro</Button>
                  <Button onClick={() => setIsCreatingForo(false)}>Cancelar</Button>
                </div>
              </form>
          </ModalDialog>
        </Modal>

        {selectedForo && (
          <div className="foros-content">
            <div className="forotitle">
              <Typography level="h3" sx={{ color: "white" }}>
                {selectedForo.forum_title}
              </Typography>
              <Typography level="body1" sx={{ color: "white" }}>
                {selectedForo.forum_description}
              </Typography>
            </div>
            <div className="forosMessages">
              {selectedForo.messages && selectedForo.messages.map((message, index) => (
                <div key={index} className="message">
                  <Typography level='body-xs'>{message.user_full_name}</Typography>
                  <div className="messageContent">
                  <Typography level="body1" sx={{ color: "white" }}>
                     {message.message_content}
                  </Typography>
                  </div>
                </div>
              ))}
            </div>
            <div className="sendMessage">
              <div className="actions">
                <Input
                  value={message.message_content}
                  onChange={(e) =>
                    setMessage({ message_content: e.target.value })
                  }
                  label="Escribir mensaje"
                  required
                />
                <Button onClick={sendMessage}>Enviar</Button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Foros;
