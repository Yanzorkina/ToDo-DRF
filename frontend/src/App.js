import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import TodoList from './components/todo.js';
import ProjectList from './components/Project.js';
import NotFound404 from './components/NotFound404.js';
import LoginForm from "./components/Auth";
import TopNavPanel from './components/Menu.js';
import Footer from './components/Footer.js';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
import axios from 'axios';
import Cookies from "universal-cookie"


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'todoes': [],
            'projects': [],
            'token': ''
        }
    }

    logout() {
        this.set_token('')
        this.set_token({'authors':[]})
        this.set_token({'todoes':[]})
        this.set_token({'projects':[]})
    }

    is_auth () {
        return !!this.state.token
    }

    set_token(token) {
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    get_token_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        const data = {username: username, password: password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


  load_data(){
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors/',{headers}).then(response => {

              this.setState(
              {
                'authors': response.data
              }
            )
          }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo_filter/',{headers}).then(response => {

                this.setState(
              {
                'todoes': response.data
              }
            )
          }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project_filter/',{headers}).then(response => {

              this.setState(
              {
                'projects': response.data
              }
            )
          }).catch(error => console.log(error))
  }

  componentDidMount() {
    this.get_token_storage()
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
                  <li> {this.is_auth() ?<button onClick={()=> this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}</li>
              </nav>
              <Routes>
                  <Route exact path='/authors' element={<AuthorList authors={this.state.authors}/>}/>
                  <Route exact path='/todoes' element={<TodoList todoes={this.state.todoes}/>}/>
                  <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                  <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
                  <Route path='*' element={<NotFound404/>}/>
              </Routes>
          </BrowserRouter>
          <Footer/>
      </div>
    )
  }
}
export default App;
