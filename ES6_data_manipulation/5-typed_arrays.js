export default function createInt8TypedArray(length, position, vaule) {
  if (position > length || position < 0) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);
  view.setInt8(position, vaule);
  return view;
}
