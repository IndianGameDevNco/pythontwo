document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  if (!form) return;

  const categoryRadios = form.querySelectorAll('input[name="category"]');
  if (!categoryRadios.length) return;

  categoryRadios.forEach((radio) => {
    radio.addEventListener("change", () => {
      if (!radio.checked) return;

      const category = radio.value;

      fetch("/units/api")
        .then((res) => res.json())
        .then((units) => {
          const unitList = units[category];
          if (!unitList) return;

          const toggleGroups = form.querySelectorAll(
            ".toggle-group, .temp, h3",
          );
          toggleGroups.forEach((group, i) => {
            if (i > 0) group.remove();
          });

          const createGroup = (c) => {
            const Group = document.createElement("div");
            Group.className = "toggle-group";

            unitList.forEach((unit, i) => {
              const id = `${unit}-${Math.random().toString(36).slice(2, 8)}`;

              const input = document.createElement("input");
              input.type = "radio";
              input.id = id;
              input.name = `unit${c}`;
              input.value = unit;
              if (i === 0) input.checked = true;

              const unitLabel = document.createElement("label");
              unitLabel.htmlFor = id;
              unitLabel.className = "toggle-label";
              unitLabel.textContent =
                unit.charAt(0).toUpperCase() + unit.slice(1);

              Group.appendChild(input);
              Group.appendChild(unitLabel);
            });

            return Group;
          };

          const firstGroup = form.querySelector(".toggle-group");

          for (let i = 0; i < 3; i++) {
            const br = document.createElement("br");
            br.className = "temp";
            if (i === 0) br.id = "last-br";
            form.insertBefore(br, firstGroup.nextSibling);
          }

          const unitGroup = createGroup(1);
          const last_br = document.querySelector("#last-br");
          form.insertBefore(unitGroup, last_br.nextSibling);

          const h3 = document.createElement("h3");
          h3.textContent = "to";
          form.insertBefore(h3, unitGroup.nextSibling);

          const unitGroup2 = createGroup(2);
          form.insertBefore(unitGroup2, h3.nextSibling);
        });
    });
  });
});
