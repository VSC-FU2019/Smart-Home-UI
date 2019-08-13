const express = require('express');
const app = express();
var http = require('http').createServer(app);
var io = require('socket.io')(http);
var mqtt = require('mqtt')

app.use('/static', express.static(__dirname + '/static'));
app.use('/manifest.json', express.static(__dirname + '/manifest.json'));
var client = mqtt.connect('mqtt://192.168.1.100:1883')


http.listen(3000, function () {
    console.log('listening on *:3000');
});


app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

client.on('connect', function () {
    console.log("connected mqtt");
    client.subscribe('light', function (err) {
    })
    client.subscribe('fan', function (err) {
    })
    client.subscribe('gate', function (err) {
    })
    client.subscribe('tivi', function (err) {
    })
    client.subscribe('door', function (err) {
    })
    client.subscribe('airconditioner', function (err) {
    })
})

client.on('message', function (topic, message) {
    // message is Buffer
    // command = message.toString()
    // if(command == '1'){
    //     io.emit('command',{command:"light_on"})
    // }else if (command=='2'){
    //     io.emit('command',{command:"light_off"})
    // }
    // else if (command=='3'){
    //     io.emit('command',{command:"airconditioner_on"})
    // }
    // else if (command=='4'){
    //     io.emit('command',{command:"airconditioner_off"})
    // }
    // else if (command=='5'){
    //     io.emit('command',{command:"fan_on"})
    // }
    // else if (command=='6'){
    //     io.emit('command',{command:"fan_off"})
    // }
    // else if (command=='7'){
    //     io.emit('command',{command:"tivi_on"})
    // }
    // else if (command=='8'){
    //     io.emit('command',{command:"tivi_off"})
    // }
    // else if (command=='9'){
    //     io.emit('command',{command:"door_open"})
    // }
    // else if (command=='10'){
    //     io.emit('command',{command:"door_close"})
    // }
    // else if (command=='11'){
    //     io.emit('command',{command:"door_lock"})
    // }
    // else if (command=='12'){
    //     io.emit('command',{command:"gate_open"})
    // }
    // else if (command=='13'){
    //     io.emit('command',{command:"gate_close"})
    // }
    // else if (command=='14'){
    //     io.emit('command',{command:"gate_lock"})
    // }
    // else if (command=='15'){
    //     io.emit('command',{command:"Doremon"})
    // }
    console.log(topic + "_" + message);
    io.emit('data', topic + "_" + message)
    io.emit('logs', topic + "_" + message)
})

io.on('connection', function (socket) {
    console.log('a user connected');
    socket.on('disconnect', function () {
        console.log('user disconnected');
    });


});