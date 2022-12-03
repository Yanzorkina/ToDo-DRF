import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import TodoList from './components/todo.js';
import ProjectList from './components/Project.js';
import NotFound404 from './components/NotFound404.js';
import TopNavPanel from './components/Menu.js';
import Footer from './components/Footer.js';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
import axios from 'axios';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
        'authors': [],
        'todoes': [],
        'projects': []

    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/authors/')
      .then(response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors
          }
        )
      }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/todo_filter/')
      .then(response => {
        this.setState(
          {
            'todoes': response.data
          }
        )
      }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/project_filter/')
      .then(response => {
        this.setState(
          {
            'projects': response.data
          }
        )
      }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
          <TopNavPanel/>
          <BrowserRouter>
              <nav>
                  <li><Link to='/authors'>Authors</Link></li>
                  <li><Link to='/todoes'>Todoes</Link></li>
                  <li><Link to='/projects'>Projects</Link></li>
              </nav>
              <Routes>
                  <Route exact path='/authors' element={<AuthorList authors={this.state.authors}/>}/>
                  <Route exact path='/todoes' element={<TodoList todoes={this.state.todoes}/>}/>
                  <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                  <Route path='*' element={<NotFound404/>}/>
              </Routes>
          </BrowserRouter>
          <Footer/>
      </div>
    )
  }
}
export default App;
