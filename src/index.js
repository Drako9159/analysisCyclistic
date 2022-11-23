
const readline = require("readline");
const fs = require("fs");
const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("certificate", "root", "password", {
  host: "localhost",
  port: 3306,
  user: "root",
  password: "password",
  dialect: "mysql",
});
const insertData = async () => {
  await sequelize.authenticate();
  const file = readline.createInterface(
    fs.createReadStream("./csv/202209-divvy-publictripdata.csv")
  );
  const datas = [];
  file.on("line", async (line) => {
    datas.push(line.split(","));
  });
  file.on("close", async () => {
    await sequelize.query({
      query:
        "INSERT INTO data202209 (ride_id, rideable_type, started_at, ended_at, start_station_name, start_station_id, end_station_name, end_station_id, start_lat, start_lng, end_lat, end_lng, member_casual) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
      values: [datas],
    });
  });

};
insertData();
