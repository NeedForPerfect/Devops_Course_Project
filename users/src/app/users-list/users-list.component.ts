import {Component, OnInit} from '@angular/core';
import {CommonModule, NgForOf} from "@angular/common";
import {UsersApiService} from "../users-api.service";
import {map} from "rxjs";
import {RouterLink, RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-users-list',
  standalone: true,
    imports: [
        NgForOf, CommonModule, RouterLink
    ],
  templateUrl: './users-list.component.html',
  styleUrl: './users-list.component.scss'
})
export class UsersListComponent implements  OnInit  {
  users: any[] = [];
  constructor(
    private usersApi: UsersApiService
  ) {}

  ngOnInit() {
    this.getUsers();
  }
  getUsers(): void {
    this.usersApi.getUsers()
        .pipe(map(res => res.map(
          (user: any) => (
            {...user,
              created_at: `${new Date(user.created_at).toDateString()} at
               ${new Date(user.created_at).toISOString().split('T')[1].slice(0, 8)}`
            })
        )))
        .subscribe(res => this.users = res);
  }
  removeUser(id: number): void {
    this.usersApi.deleteUserById(id)
      .subscribe(deletedUserId => this.users = this.users.filter(user => user.id !== deletedUserId));
  }

}
