export default class HolbertonCourse {
  constructor(name, length, students) {
    if (name !== 'string') {
      throw new Error('Name must be a string');
    }

    if (typeof length !== 'number') {
      throw new Error('Length must be a number');
    }

    if (!Array.isArray(students)) {
      throw new Error('Students must be an array');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(value) {
    this._name = value;
  }

  get name() {
    return this._name;
  }

  set students(value) {
    this._students = value;
  }

  get students() {
    return this._students;
  }

  set length(value) {
    this._length = value;
  }

  get length() {
    return this._length;
  }
}
