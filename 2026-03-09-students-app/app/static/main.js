"use strict"

{
    const tbody = document.getElementById("tbody");
    
    window.addEventListener("load", getAll);
    

    async function getAll() {
        let response = await axios.get("/students");
        const students = response.data;
        let content = "";
        for (const s of students){
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