import {Component, OnInit} from '@angular/core';
import {NgIf} from "@angular/common";
import {FormControl, ReactiveFormsModule, Validators} from "@angular/forms";
import {UsersApiService} from "../users-api.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-edit-user',
  standalone: true,
    imports: [
        NgIf,
        ReactiveFormsModule
    ],
  templateUrl: './edit-user.component.html',
  styleUrl: './edit-user.component.scss'
})
export class EditUserComponent implements OnInit {
  userNameControl = new FormControl('', [Validators.required]);

  get userId(): number {
    return +this.activatedRoute.snapshot.params['id'];
  }

  constructor(
    private usersApi: UsersApiService,
    private router: Router,
    private activatedRoute: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.usersApi.getUserById(this.userId)
        .subscribe(({ user_name }) => this.userNameControl.patchValue(user_name))
  }

  editUser(): void {
    this.usersApi.updateUser(this.userId, { user_name: this.userNameControl.value })
        .subscribe(() => this.router.navigate(['users']))
  }
}
