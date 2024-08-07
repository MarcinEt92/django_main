QUnit.test('mk smoke test', (assert) => {
    assert.equal(1, 1, "Works!");
});
QUnit.test("visibility test", (assert) => {
    const err = document.querySelector(".has-error");
    const cssObj = window.getComputedStyle(err, null);
    let isVisible = cssObj.getPropertyValue("visibility");
    assert.equal(isVisible, "visible", "Visible!");

    // hide element
    document.querySelector(".has-error").style.visibility = "hidden";
    isVisible = cssObj.getPropertyValue("visibility");
    assert.equal(isVisible, "hidden", "Hidden!");
});
