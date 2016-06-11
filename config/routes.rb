Rails.application.routes.draw do
  get 'cclasses/index'

  get 'posts/index'
  root 'posts#index'
  get ':controller(/:action)'
  get 'about'   => 'posts#about'
  get 'blog'    => 'posts#blog'
  get 'contact' => 'posts#contact'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
