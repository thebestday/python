urlParams = new URLSearchParams(window.location.search);
params = {};

urlParams.forEach((p,key) => {
params[key] = p;
});
document.write(params.specialisation, '<br>')
document.write(params.sallary, '<br>')
document.write(params.location, '<br>')
document.write(params.work_place, '<br>')
document.write(params.comment, '<br>')
document.write('зарплата Python-разработчика в Москве составляет в среднем  от {}руб. до {}руб.'.format(mid_sal_from, mid_sal_to ))