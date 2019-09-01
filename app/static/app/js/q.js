const url = 'https://ghfod4drnbgjvg55tv6dtkwqiu.appsync-api.us-east-2.amazonaws.com/graphql'
const apikey = 'da2-vrrid7kj2vhovlv6fnjecpma6q'
const region = 'us-east-2'

var opts = {
  method: "GET",
  headers: { "key": apikey },
  body: JSON.stringify({ query: mutation })
};


/*const query = `
  query {
    Lift(id: "panorama") {
      name
      status
    }
  }
`;
const url = "https://snowtooth.moonhighway.com/";
const opts = {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query })
};
fetch(url, opts)
  .then(res => res.json())
  .then(console.log)
  .catch(console.error);*/