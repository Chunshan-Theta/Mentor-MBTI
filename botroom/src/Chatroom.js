// Chatroom.js
import React from 'react';

const Chatroom = ({ messages }) => {
  return (
    <div className="chatroom">
      {messages.map(message => (
        <div key={message.id} className="message">
          <p>{message.text}</p>
          <span>{message.sender}</span>
        </div>
      ))}
    </div>
  );
};

export default Chatroom;
