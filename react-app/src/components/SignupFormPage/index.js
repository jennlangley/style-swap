import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState('');
	const [lastName, setLastName] = useState('');
	const [bio, setBio] = useState('');
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
        const data = await dispatch(signUp(username, email, password, firstName, lastName, bio));
        if (data) {
          setErrors(data)
        }
    } else {
        setErrors(['Confirm Password field must be the same as the Password field']);
    }
  };

  return (
    <div className="loginContainer loginFormPage">
			<h1 id="modal-title">Sign Up</h1>
			<div>
				<form onSubmit={handleSubmit}>
					<ul className="errors">
						{errors.map((error, idx) => (
							<li key={idx}>{error}</li>
						))}
					</ul>
					<div>
						<label>
							Email
							<input
								className="inputBox loginInput"
								type="text"
								value={email}
								onChange={(e) => setEmail(e.target.value)}
								required
							/>
						</label>
					</div>
					<div>
						<label>
						Username
							<input
								className="inputBox loginInput"
								type="text"
								value={username}
								onChange={(e) => setUsername(e.target.value)}
								required
							/>
						</label>
					</div>
					<div>
						<label>
							First Name
							<input
								className="inputBox loginInput"
								type="text"
								value={firstName}
								onChange={(e) => setFirstName(e.target.value)}
								required
							/>
						</label>
					</div>
					<div>
						<label>
							Last Name
							<input
								className="inputBox loginInput"
								type="text"
								value={lastName}
								onChange={(e) => setLastName(e.target.value)}
								required
							/>
						</label>
					</div>
					<div>
						<label>
							Bio
							<textarea
								className="inputBox loginInput textarea"
								type="text"
								value={bio}
								onChange={(e) => setBio(e.target.value)}
								required
							/>
						</label>
					</div>
					<div>
						<label>
						Password
							<input
								className="inputBox loginInput"
								type="password"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
								required
							/>
						</label>
					</div>
					
					<label>
						Confirm Password
						<input
							className="inputBox loginInput"
							type="password"
							value={confirmPassword}
							onChange={(e) => setConfirmPassword(e.target.value)}
							required
						/>
					</label>
					<button className="confirmButtonDesign formButton" type="submit">Sign Up</button>
				</form>
			</div>
		</div>
  );
}

export default SignupFormPage;
