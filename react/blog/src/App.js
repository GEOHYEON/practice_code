import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  let [title, editTitle] = useState(['남자 코트 추천', '여자 코트 추천', '어린이 코트 추천']);
  let [good, editGood] = useState(0);
  function hello_world() {
    return 'Hello, world.'
  }

  return (
    <div className="App">
      <div className="black-nav">
        <div>blog</div>
      </div>
      <p>{hello_world()}</p>
      <div className='list'>
        <h4>{ title[0] } <span onClick={()=>{editGood(good+1)}}>good</span> {good} </h4>
        <p>3월 10일</p>
        <hr/>
      </div>
      <div className='list'>
        <h4>{ title[1] }</h4>
        <p>3월 11일</p>
        <hr/>
      </div>
      <div className='list'>
        <h4>{ title[2] }</h4>
        <p>3월 12일</p>
        <hr/>
      </div>
    </div>
  );
}

export default App;
