let serialport = require("serialport");
const { ReadlineParser } = require('@serialport/parser-readline')
let SerialPort = serialport.SerialPort;
let portName = process.argv[2];

let myPort = new SerialPort({
    path: "COM11"}
);

const parser = myPort.pipe(new ReadlineParser({ delimiter: '\r\n' }))

parser.on(4, console.log);

function onData(data){
    console.log("on Data" + data);
}