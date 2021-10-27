const um = document.getElementById('prim')
const dois = document.getElementById('sec')
const tres = document.getElementById('terc')
const quatro = document.getElementById('qrt')
const cinco = document.getElementById('qnt')

const arr = [um, dois, tres, quatro, cinco]
const form = document.querySelector('.rate-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const manipularSelecao = (size) => {
    const children = form.children

    for(let i=0; i < children.length;i++){
      if(i <= size){
        children[i].classList.add('checked')
      }else{
        children[i].classList.remove('checked')
      }
    }
}

const Selecionar = (selection) => {
    switch(selection){
      case 'prim':{
        manipularSelecao(1)
      // um.classList.add('checked')
      // dois.classList.remove('checked')
      // tres.classList.remove('checked')
      // quatro.classList.remove('checked')
      // cinco.classList.remove('checked')
      return
    }

      case 'sec':{
        manipularSelecao(2)
      return
    }

      case 'terc':{
        manipularSelecao(3)
      return
    }

      case 'qrt':{
        manipularSelecao(4)
      return
    }

      case 'qnt':{
        manipularSelecao(5)
      return
    }
    }
}

const getNumericValue = (stringValue) =>{
  let numericValue;
  if (stringValue=='prim'){
    numericValue = 1;
  }
  else if (stringValue=='sec'){
    numericValue = 2;
  }
  else if (stringValue=='terc'){
    numericValue = 3;
  }
  else if (stringValue=='qrt'){
    numericValue = 4;
  }
  else if (stringValue=='qnt'){
    numericValue = 5;
  }
  else {
    numericValue = 0;
  }
  return numericValue
}


if(um){
  arr.forEach(item => item.addEventListener('mouseover', (event) =>{  Selecionar(event.target.id)   }))
  arr.forEach(item => item.addEventListener('click', (event) =>{
      const val = event.target.id
      let is_Submit = false

      form.addEventListener('submit', (e) =>{
        e.preventDefault()
        if(is_Submit){
          return
        }

        is_Submit = true


        const id = e.target.id
        const val_num = getNumericValue(val)



        $.ajax({
          type: 'POST',
                url: '/avaliar/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': id,
                    'val': val_num,
                },
                success: function(response){
                    console.log(response)
                    confirmBox.innerHTML = `<h1>Successfully rated with ${response.score}</h1>`
                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML = '<h1>Ups... something went wrong</h1>'
                }
        })


      })


   }))
}
