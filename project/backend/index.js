const express = require("express");
const { Pool } = require("pg");

const app = express();

const pool = new Pool({
  host: "postgres",
  user: "appuser",
  password: "secret",
  database: "appdb"
});

app.get("/", async (req, res) => {
  await pool.query("SELECT 1");
  res.send("Node.js aplikacja działa 🚀");
});

app.listen(3000, "0.0.0.0", () => {
  console.log("Backend listening on port 3000");
});

