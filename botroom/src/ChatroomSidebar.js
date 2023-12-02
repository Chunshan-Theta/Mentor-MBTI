// ChatroomSidebar.js
import React from 'react';

const ChatroomSidebar = () => {
  const tips = [
    { id: 1, title: '歡迎來到文字冒險遊戲' , content: '請透過聊天室進行遊玩，先跟我說個`hi`來開始吧！' },
    // Add more rooms as needed
  ];
  
  return (
    <div className="sidebar">
      <h2>Chat Step</h2>
      <ul>
        {tips.map(tip => (
          <li>
            <div key={tip.id} >
              <p>{tip.title}</p>
              <p>{tip.content}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatroomSidebar;
