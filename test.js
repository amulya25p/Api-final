const Twilio = require("twilio");
const client = new Twilio("ACce76adada8f41929681a785bb386fe67","9137a187d5f7f2b3992c5bb419aac5f4");
client.messages.list().then(messages => console.log(`The most recent message is ${messages[0].body}`));
console.log("Gathering your message log");