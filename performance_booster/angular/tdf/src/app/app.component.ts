import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
  
export class AppComponent implements OnInit {
  title = 'tdf';

  contact: contact;
  showMsg: boolean = false;

  ngOnInit() {
    this.contact = {
      firstname: "MJ Ekua",
      lastname: "Jonah",
      email: "mary.jonah@turntabl.io",
      isToc: true
    }
  }

  onSubmit() {
    console.log(this.contact)
    this.showMsg = true;
  }
  
}

export class contact {
  firstname: string;
  lastname: string;
  email: string;
  isToc: boolean;
}

