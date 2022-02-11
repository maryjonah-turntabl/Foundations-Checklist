import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'mdf';
  showMsg: boolean = false;

  contactForm = new FormGroup({
    firstname: new FormControl("Mary", [Validators.required, Validators.pattern("^[a-zA-Z]+$")]),
    lastname: new FormControl("Jonah", [Validators.required, Validators.pattern("^[a-zA-Z]+$")]),
    email: new FormControl("test@turtabl.io",[Validators.required, Validators.email]),
    isToc: new FormControl(true, [Validators.required])
  })

  get firstname() {
    return this.contactForm.get('firstname')
  }
  get lastname() {
    return this.contactForm.get('lastname')
  }
  get email() {
    return this.contactForm.get('email')
  }
  get isToc() {
    return this.contactForm.get('isToc')
  }


  onSubmit() {
    console.log(this.contactForm.value);
    this.showMsg = true;
  }
}

