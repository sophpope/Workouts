import {useState} from 'react';

function addUserForm({addUser}) {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        
        if (!username.trim()){
            setError("Please enter a username")
            return
        }else if(!email.trim()){
            setError("Please enter an email address")
            return
        }else if(!password.trim()){
            setError("Please enter a password")
            return
        }
        onSubmit(username, email, password);
    };

    return <div className = "user-input-container">
    <h2>Please create your user</h2>
    <p>Enter your user details</p>
    <form onSubmit={handleSubmit}>
        <div className='user-group'>
            <input
                type = "text"
                value = {username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder='Enter your username'
                className = {error && !userame ? 'error': ''}
                />
        </div>
        <div>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder='Enter your email address'
                className={error && !email ? 'error': ''}
                />
        </div>
        <div>
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder='Enter your password'
                className={error && !password ? 'error': ''}
                />
        </div>
        <button type="sumbit" className='generate-btn'>
            Submit user details 
        </button>
    </form>
    </div>

}

export default addUserForm