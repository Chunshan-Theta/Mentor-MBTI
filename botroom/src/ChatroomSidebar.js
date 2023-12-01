// ChatroomSidebar.js
import React from 'react';

const ChatroomSidebar = ({ rooms, changeRoom }) => {
  return (
    <div className="sidebar">
      <h2>Chat Rooms</h2>
      <ul>
        {rooms.map(room => (
          <li key={room.id} onClick={() => changeRoom(room.id)}>
            {room.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatroomSidebar;
