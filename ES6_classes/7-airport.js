export default class Airport {
  /**
     *
     * @param {String} name
     * @param {String} code
     */
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    return `[Object ${this._code}]`;
  }
}
