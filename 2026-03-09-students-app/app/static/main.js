"use strict"

{
    const tbody = document.getElementById("tbody");
    // get reference to inputs and buttons
    const idBox = document.getElementById("idBox");
    const nameBox = document.getElementById("nameBox");
    const ageBox = document.getElementById("ageBox");
    const btAdd = document.getElementById("btAdd");
    const btUpdate = document.getElementById("btUpdate");
    const btDelete = document.getElementById("btDelete");

    btAdd.addEventListener("click", async function () {
        const name = nameBox.value;
        const age = ageBox.value;
        if (!name || !age) {
            alert("Enter name and age!");
            return;
        }
        const student = { name, age };
        const response = await axios.post("/students", student);
        getAll();
    });

    btDelete.addEventListener("click", async function () {
        const id = idBox.value;
        if (!id) {
            alert("Enter ID!");
            return;
        }
        try {
            await axios.delete(`/students/${id}`);
            getAll();
        } catch (error) {
            //console.dir(error);
            alert(error.response.data.message);
        }
    })

    window.addEventListener("load", getAll);


    async function getAll() {
        let response = await axios.get("/students");
        const students = response.data;
        let content = "";
        for (const s of students) {
            content += `
                <tr>
                  <td>${s.id}</td>
                  <td>${s.name}</td>
                  <td>${s.age}</td>
                </tr>
            `;
        }
        tbody.innerHTML = content;

    }
}