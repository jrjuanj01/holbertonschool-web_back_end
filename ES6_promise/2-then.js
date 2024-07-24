export default function handleResponseFromAPI(promise) {
  return promise.then(
    console.log('Got a response from the API'),
    ({ status: 200, body: 'Success' })
  ).catch(() => {
    console.log('Got a response from the API');
    return (Error)
  });
}
