export default function handleResponseFromAPI(promise) {
  return promise.then(
    { status: 200, body: 'Success' },
    console.log('Got a response from the API'),
  ).catch(() => {
    console.log('Got a response from the API');
  });
}
