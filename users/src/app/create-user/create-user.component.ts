import { Component } from '@angular/core';
import {FormControl, ReactiveFormsModule, Validators} from "@angular/forms";
import {UsersApiService} from "../users-api.service";
import {Router} from "@angular/router";
import {NgIf} from "@angular/common";

@Component({
  selector: 'app-create-user',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf],
  templateUrl: './create-user.component.html',
  styleUrl: './create-user.component.scss'
})
export class CreateUserComponent {
  userNameControl = new FormControl('', [Validators.required]);

  constructor(
    private usersApi: UsersApiService,
    private router: Router,
  ) {
  }

  createUser(): void {
    this.usersApi.createUser({ user_name: this.userNameControl.value })
        .subscribe(() => this.router.navigate(['users']))
  }

}
