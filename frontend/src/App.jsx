import React, { useState } from 'react'

const API_BASE = import.meta.env.VITE_API_BASE || ''

export default function App() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [token, setToken] = useState('')
  const [error, setError] = useState('')

  const login = async (e) => {
    e.preventDefault()
    setError('')
    setToken('')
    try {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      })
      if (!res.ok) throw new Error('Login failed')
      const data = await res.json()
      setToken(data.access_token)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div style={{ maxWidth: 360, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>JAL Admin Login</h1>
      <form onSubmit={login}>
        <div>
          <label>Email</label>
          <input value={email} onChange={e => setEmail(e.target.value)} type="email" required />
        </div>
        <div>
          <label>Password</label>
          <input value={password} onChange={e => setPassword(e.target.value)} type="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {token && (
        <div>
          <p>Token:</p>
          <textarea readOnly rows={6} cols={40} value={token} />
        </div>
      )}
    </div>
  )
}
