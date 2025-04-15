const DateTime = luxon.DateTime;

Telegram.WebApp.ready();

// Календарь
flatpickr("#datepicker", {
  dateFormat: "Y-m-d",
  defaultDate: new Date(),
  onChange: (selectedDates, dateStr, instance) => instance.close()
});

// Таймпикер
flatpickr("#timepicker", {
  enableTime: true,
  noCalendar: true,
  dateFormat: "H:i",
  time_24hr: true,
  defaultDate: "12:00",
  onChange: (selectedDates, dateStr, instance) => instance.close()
});

// Кнопка "Готово"
document.getElementById("doneBtn").addEventListener("click", () => {
  const date = document.getElementById("datepicker").value;
  const time = document.getElementById("timepicker").value;
  const zone = document.getElementById("timezone").value;

  if (!date || !time) {
    alert("Пожалуйста, выберите дату и время");
    return;
  }

  const iso = `${date}T${time}:00`;
  const dt = DateTime.fromISO(iso).setZone(zone);

  const data = {
    iso,
    formatted: dt.toFormat("yyyy-LL-dd HH:mm ZZZZ"),
    timezone: zone
  };

  Telegram.WebApp.sendData(JSON.stringify(data));
  Telegram.WebApp.close();
});
